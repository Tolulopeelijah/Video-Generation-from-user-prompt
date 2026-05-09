from groq import Groq


SYSTEMS_PROMPT = """you are a professional video designer, your job is to take a script and transform it to a manim code, using interactive and intuitive 
                    designs, ensure that the objects do not overlap, you can make use of images, 3d materials, backgrounds, foregrounds (referrred to as assets),... 
                    you can get a list of avaialble asset and what they represent using a tool call, if an asset in needed but not available in the existing assets,
                    call the asset_generation agent to fetch it.
                    return a highly professional video desing in manim code format, and double check for errors and dimensions overlapping
                    """



def 