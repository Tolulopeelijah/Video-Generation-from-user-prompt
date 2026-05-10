import subprocess
import tempfile
import os
import re

class ManimVideoRenderer:
    def render_manim_code(self, manim_code, output_filename="output_video"):
        """
        Render Manim code to video
        
        Args:
            manim_code (str): String containing Manim code
            output_filename (str): Desired output filename (without extension)
        
        Returns:
            str: Path to the generated video file
        """
        # Extract scene class name from code
        scene_match = re.search(r'class\s+(\w+)\s*\(\s*Scene\s*\)', manim_code)
        if not scene_match:
            raise ValueError("No Scene class found in the code")
        
        scene_name = scene_match.group(1)
        
        # Create a temporary file for the Manim code
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(manim_code)
            temp_file = f.name
        
        try:
            # Render the video using manim command
            cmd = [
                "manim",
                "-ql",  # -qh for high quality 
                "--output_file", output_filename,
                temp_file,
                scene_name
            ]
            
            # Run manim command
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"Error rendering: {result.stderr}")
                return None
            
            # Find the generated video file
            video_dir = "media/videos"
            for root, dirs, files in os.walk(video_dir):
                for file in files:
                    if file.endswith('.mp4') and output_filename in file:
                        video_path = os.path.join(root, file)
                        print(f"✅ Video created: {video_path}")
                        return video_path
            
            print("⚠️ Video file not found")
            return None
            
        finally:
            # Clean up temporary file
            os.unlink(temp_file)