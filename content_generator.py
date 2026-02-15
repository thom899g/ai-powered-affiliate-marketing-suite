import logging
from typing import Dict, Any
from ai_model_wrapper import AIModelWrapper

class ContentGenerator:
    def __init__(self):
        self.ai_model = AIModelWrapper()
        self.logger = logging.getLogger(__name__)

    def generate_text_content(self, product_data: Dict[str, str]) -> str:
        """Generates tailored promotional text content."""
        try:
            response = self.ai_model.generate(
                f"Create a compelling promotional description for {product_data['name']}."
            )
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Failed to generate text content: {str(e)}")
            return "Unable to generate content at this time."

    def generate_html_content(self, product_data: Dict[str, str]) -> str:
        """Generates tailored promotional HTML content."""
        try:
            template = f"""
            <div style="padding:20px;">
                <h1>{product_data['name']}</h1>
                <p>Discover {product_data['features']}</p>
                <a href="{product_data['link']}">Learn More</a>
            </div>
            """
            return self._apply_styling(template)
        except Exception as e:
            self.logger.error(f"Failed to generate HTML content: {str(e)}")
            return "Unable to generate content at this time."

    def _apply_styling(self, template: str) -> str:
        """Applies styling to the HTML template."""
        # Placeholder for actual styling logic
        pass

    def generate_image_content(self, product_data: Dict[str, str]) -> bytes:
        """Generates tailored promotional image content."""
        try:
            response = self.ai_model.generate_image(product_data['description'])
            return response.image.data
        except Exception as e:
            self.logger.error(f"Failed to generate image content: {str(e)}")
            return b"Unable to generate image at this time."