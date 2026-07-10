from schemas import SnapshotStructureResult

def snapshot_structure_validation(parsed_keys: set[str], expected_keys: set[str]) -> SnapshotStructureResult:
    """
    Comparing parsed keys with expected keys for the structure confirmation
    Args:
        parsed_keys (set[str]): keys for check
        expected_keys (set[str]): expected keys

    Returns:
       SnapshotStructureResult: dataclass for handed over errors to pipeline
    """
    
    errors = []
    if not parsed_keys:
        return SnapshotStructureResult(
            ok=False,
            errors=[f"No parsed keys for comparing"]
        )

    if not expected_keys:
        return SnapshotStructureResult(
            ok=False,
            errors=[f"No expected keys for comparing"]
        )
    
    missing_keys = expected_keys - parsed_keys
    extra_keys = parsed_keys - expected_keys
    
    if missing_keys:
        errors.append(f"Missing keys in parsed data: {sorted(missing_keys)}")

    if extra_keys:
        errors.append(f"Extra keys in parsed data: {sorted(extra_keys)}")        
        
    return SnapshotStructureResult(
        ok=not errors,
        errors=errors,
        )
    
  
  
  
  
  
  
  
  
