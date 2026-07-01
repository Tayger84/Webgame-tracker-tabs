from validation.validation_overview import overview_structure_validation
from parsers.overview import load_alliance_overview_data
from schemas import OverviewPipelineResult
# from pathlib import Path
from bs4 import BeautifulSoup

# DATA_URL = Path(__file__).parents[1] / "tests" / "fixtures" / "overview_parser_test_data" / "original_NTRLTY_aliance.html"

# html = DATA_URL.read_text(encoding="utf-8")

def process_overview_alliance(html: str) -> OverviewPipelineResult:
    """
    Overview Alliance data processing function

    Args:
        html (str): offline html record

    Returns:
        OverviewPipelineResult: Overview Alliance data output with errors list
    """
    
    if not html:
        return OverviewPipelineResult(
            ok=False,
            errors=["No HTML file was imported"]
        )

    if not bool(BeautifulSoup(html, "html.parser").find()):
        return OverviewPipelineResult(
            ok=False,
            errors=["The source file is not in HTML format"]
        )
        
    parser_result = load_alliance_overview_data(html)
    
    if not parser_result.ok:
        return OverviewPipelineResult(
            ok=False,
            errors=["The parsing process failed"] + parser_result.errors
        )

    validation_result = overview_structure_validation(parser_result.data)
    
    if not validation_result.ok:
        return OverviewPipelineResult(
            ok=False,
            errors=["Found some errors during validation process"] + validation_result.errors
        )
        
    return OverviewPipelineResult(
        ok=True,
        data=parser_result.data
    )

    
    
        





