from schemas import SnapshotPipelineResult
from bs4 import BeautifulSoup
from parsers.snapshot import load_alliance_snapshot_data
from validation.validation_snapshot import snapshot_structure_validation
from contracts.snapshot import METRIC_KEYS

def process_snapshot_alliance(html: str) -> SnapshotPipelineResult:
    """
    Snapshot Alliance data processing function

    Args:
        html (str): offline html record

    Returns:
        SnapshotPipelineResult: Overview Alliance data output with errors list
    """
    
    if not html:
        return SnapshotPipelineResult(
            ok=False,
            errors=["No HTML file was imported"],
        )
        
    if not bool(BeautifulSoup(html, "html.parser").find()):
        return SnapshotPipelineResult(
            ok=False,
            errors=["The source file is not in HTML format"]
        )
        
    parser_result = load_alliance_snapshot_data(html)
    
    if not parser_result.ok:
        return SnapshotPipelineResult(
            ok=False,
            errors=["The parser process failed"] + parser_result.errors,
        )   
        
    validation_result = snapshot_structure_validation(set(METRIC_KEYS), set(parser_result.data.parsed_keys))
    
    if not validation_result.ok:
        return SnapshotPipelineResult(
            ok=False,
            errors=["Found some errors during validation process"] + validation_result.errors
        )
    
    return SnapshotPipelineResult(
        ok=True,
        data=parser_result.data,
        errors=parser_result.errors,
    )
