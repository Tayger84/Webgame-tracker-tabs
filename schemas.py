from dataclasses import dataclass, field

# Start loaded webpage function
@dataclass(frozen=True)
class TimeDataResult:
    ok: bool
    data: str | None = None
    error: str | None = None
# End loaded webpage function

# Start Age parsering dataclasses
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
    
# End Age parsering dataclasses

# Start Alliance Overview parsering dataclasses
@dataclass(frozen=True)
class AllianceOverviewData:
        country_number: int | None = None
        alliance_name: str | None = None
        country_name: str | None = None
        country_area: str |None = None
        country_prestige: str | None = None
        player_name: str | None = None
        regime: str | None = None

@dataclass(frozen=True)
class AllianceOverviewResult:
    ok: bool
    data: dict[int, AllianceOverviewData] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    # raw_values: list[str] = field(default_factory=list)

@dataclass(frozen=True)    
class OverviewStructureResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    
@dataclass(frozen=True)
class OverviewPipelineResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    data: AllianceOverviewData | None=None
    row_values: list[str] = field(default_factory=list)
    
# End Alliance Overview parsering dataclasses

# Start Alliance Snapshot parsering dataclasses

@dataclass(frozen=True)
class AllianceSnapshotData:
    country_number: list[str] = field(default_factory=list)
    parsed_keys: list[str] = field(default_factory=list)
    snapshot_data: list[str] = field(default_factory=list)
    
@dataclass(frozen=True)
class AllianceSnapshotResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    data: AllianceSnapshotData | None = None


# End Alliance Parsing parsering dataclasses