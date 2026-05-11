# Agent calls this tool
asset_tool = AssetManagementTool()

# Get asset (automatically handles cache/gen)
response = asset_tool.execute(
    asset_type="manim_video",
    generation_params={
        "code": "your_manim_code_here",
        "quality": "1080p"
    }
)

if response['success']:
    video_path = response['path']
    # Use the asset...