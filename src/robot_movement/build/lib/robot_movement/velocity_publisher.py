#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from queue import Queue
import time

#Stuff for speech recognition
import whisper
import sounddevice as sd 
import soundfile as sf 


class InstructionsNode(Node):
    def __init__(self):
        super().__init__("node_inst_pub")
        self.cmd_inst_pub = self.create_publisher(String, "instruction_topic", 10)
        #The function is called every 0.5 seconds
        self.timer = self.create_timer(0.5, self.send_info) 

        #AI Speech recognition Model
        self.model = whisper.load_model("base")
        self.audio_file_path = "audio.wav"      #Required for select/edit the audio file
        
        self.recording_start_time = None
        self.recording_duration = 3             #Duration for the recording
        self.get_logger().info("Node_inst_pub has been opened")
        self.instruction_list = {"forward", "backward", "stop"}
        self.instruction_queue = Queue()
        self.instruction = "stop"
        self.flag = False

    def send_info(self):
        msg = String()

        if not self.instruction_queue.empty():
            msg.data = self.instruction_queue[0]
            self.instruction = self.instruction_queue[0]
            self.instruction_queue.pop(0)
        else:
            msg.data = self.instruction
        self.cmd_inst_pub.publish(msg)

        if self.is_recording_finished():
            self.record_audio()
            self.recognize_speech()

    def record_audio(self):
        self.get_logger().info("Recording...")
        self.recording_start_time = time.time()
        audio_data = sd.rec(int(44100 * self.recording_duration), samplerate=44100, channels=2, dtype='float64')
        sd.wait()
        
        if len(audio_data.shape) == 1:
            audio_data = audio_data.reshape(-1, 1)  # Convertir a dos dimensiones
        sf.write(self.audio_file_path, audio_data, 44100)
        self.flag = True

    def is_recording_finished(self):
        if self.recording_start_time is None:
            return True  # Si no ha comenzado la grabación, se considera como finalizada
        else:
            elapsed_time = time.time() - self.recording_start_time
            return elapsed_time >= self.recording_duration

    def recognize_speech(self):
        if self.flag:
            self.get_logger().info("Speech recognition...")  
            audio = whisper.load_audio(self.audio_file_path)
            audio = whisper.pad_or_trim(audio)

            # make log-Mel spectrogram and move to the same device as the model
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
            options = whisper.DecodingOptions()
            self.transform_speech(whisper.decode(self.model, mel, options))
            self.flag = False

    
    def transform_speech(self, text):
        words = text.split()
        instruction_found = [instruction for instruction in words if instruction.lower() in self.instruction_list]
        
        for instruccion in instruction_found:
            self.instruction_queue.put(instruccion)


def main(args=None):

    #Parameters reqwuired for speech recognition
    rclpy.init(args=args)
    node = InstructionsNode()

    node.send_info()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()