from mindmate.services.models import Writing, Image, Video, Prompt, Design, Presentation, NoCodeDevelopmentPlatform, Data, DevelopmentPlatform
from mindmate.utils.utils import utility

class manifest:
    def list_writing() -> dict:
        result = Writing.get_all()
        final = utility.extract_results(result)
        return final
    def list_images() -> dict:
        result = Image.get_all()
        final = utility.extract_results(result)
        return final
    def list_videos() -> dict:
        result = Video.get_all()
        final = utility.extract_results(result)
        return final
    def list_prompting() -> dict:
        result = Prompt.get_all()
        final = utility.extract_results(result)
        return final
    def list_designs() -> dict:
        result = Design.get_all()
        final = utility.extract_results(result)
        return final
    def list_presentations() -> dict:
        result = Presentation.get_all()
        final = utility.extract_results(result)
        return final
    def list_no_code() -> dict:
        result = NoCodeDevelopmentPlatform.get_all()
        final = utility.extract_results(result)
        return final
    def list_data() -> dict:
        result = Data.get_all()
        final = utility.extract_results(result)
        return final
    def list_development() -> dict:
        result = DevelopmentPlatform.get_all()
        final = utility.extract_results(result)
        return final