from dataclasses import dataclass, field

# start Age parsering dataclass 
@dataclass(frozen=True)
class AgeTimeData:
    name: str | None = None
    start: str | None = None
    end: str | None = None
    rest_time: str | None = None
    
@dataclass(frozen=True)
class AgeTimeResult:
    ok: bool
    data: AgeTimeData | None = None
    errors: list[str] = field(default_factory=list)
    raw_values: list[str] = field(default_factory=list)
    
@dataclass(frozen=True)
class AgeStructureResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    
@dataclass(frozen=True)
class AgePipelineResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    data: AgeTimeData | None = None
    raw_values: list[str] = field(default_factory=list)
    
# end Age parsering dataclass