from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASecurity(BaseDMAType):
    """
    Represents DMA Security.

    Attributes:
        StartElement (Optional[bool]): Whether or not the user is allowed to start elements.
        StopElement (Optional[bool]): Whether or not the user is allowed to stop elements.
        PauseElement (Optional[bool]): Whether or not the user is allowed to pause elements.
        MaskElementUntilClearance (Optional[bool]): Whether or not the user is allowed to mask elements until clearance.
        MaskElementUntilUnmasking (Optional[bool]): Whether or not the user is allowed to mask elements until unmasking.
        UnmaskElement (Optional[bool]): Whether or not the user is allowed to unmask elements.
        MaskAlarm (Optional[bool]): Whether or not the user is allowed to mask alarms.
        AlarmUnmasking (Optional[bool]): Whether or not the user is allowed to unmask alarms.
        AlarmTakeOwnership (Optional[bool]): Whether or not the user is allowed to take ownership of alarms.
        AccessElement (Optional[bool]): Whether or not the user is allowed to open elements.
        DataDisplayAccess (Optional[bool]): Whether or not the user has access to data pages.
        ServiceDataDisplayAccess (Optional[bool]): Whether or not the user has access to data pages of services.
        AccessAlarms (Optional[bool]): Whether or not the user is allowed to open alarms.
        ReleaseOwnershipOtherUser (Optional[bool]): Whether or not the user is allowed to release ownership of alarms that are being owned by other users.
        Trending (Optional[bool]): Whether or not the user has access to trending.
        Dashboards (Optional[bool]): Whether or not the user has access to DMS Dashboards
        Reporter (Optional[bool]): Whether or not the user has access to DMS Reporter
        Surveyor (Optional[bool]): Whether or not the user has access to the Surveyor.
        TicketsUI (Optional[bool]): Whether or not the user has access to DMS Ticketing.
        TicketsConfigUI (Optional[bool]): Whether or not the user is allowed to configure ticket domains.
        TicketsAddTicket (Optional[bool]): Whether or not the user is allowed to add tickets.
        TicketsEditTicket (Optional[bool]): Whether or not the user is allowed to edit tickets.
        TicketsDeleteTicket (Optional[bool]): Whether or not the user is allowed to delete tickets.
        DashboardsAdd (Optional[bool]): Whether or not the user is allowed to add dashboards.
        DashboardsEdit (Optional[bool]): Whether or not the user is allowed to edit dashboards.
        DashboardsDelete (Optional[bool]): Whether or not the user is allowed to delete dashboards.
        JobsViewAll (Optional[bool]): Whether or not the user is allowed to view all jobs.
        JobsCreateUpdateJobs (Optional[bool]): Whether or not the user is allowed to create or update jobs.
        JobsDeleteJobs (Optional[bool]): Whether or not the user is allowed to delete jobs.
        JobsCreateUpdateDeleteSections (Optional[bool]): Whether or not the user is allowed to create, update or delete job sections.
        Collaboration (Optional[bool]): Whether or not the user is allowed to use the collaboration feature.
        ViewNotes (Optional[bool]): Whether or not the user is allowed to view notes.
        ShareItem (Optional[bool]): Whether or not the user is allowed to share DataMiner items via dataminer.services.
        UnshareItem (Optional[bool]): Whether or not the user is allowed to stop the sharing of DataMiner items via dataminer.services.
        UpdateSharedItems (Optional[bool]): Whether or not the user is allowed to make changes to a share of DataMiner items via dataminer.services.
        SendEmail (Optional[bool]): Whether or not the user is allowed to send emails.
        MonitoringUI (Optional[bool]): Whether or not the user is allowed to access the Monitoring app.
        UserDefinableAppPublish (Optional[bool]): Whether or not the user is allowed to publish user-defined apps.
        UserDefinableAppEdit (Optional[bool]): Whether or not the user is allowed to edit user-defined apps.
        UserDefinableAppDelete (Optional[bool]): Whether or not the user is allowed to delete user-defined apps.
        UserDefinableAppAdd (Optional[bool]): Whether or not the user is allowed to create user-defined apps.
        UserDefinableAppView (Optional[bool]): Whether or not the user is allowed to view user-defined apps.
        ViewSharedItems (Optional[bool]): Whether or not the user is allowed to view items shared via dataminer.services.
        Security (Optional[bool]): Whether or not the user is allowed to modify security settings.
        SDAutomation (Optional[bool]): Whether or not the user is allowed to open the Automation module in DataMiner Cube and view the list of available Automation scripts in web apps.
        AutomationExecuteScripts (Optional[bool]): Whether or not the user is allowed to execute Automation scripts.
    """

    StartElement: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to start elements."},
    )
    StopElement: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to stop elements."},
    )
    PauseElement: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to pause elements."},
    )
    MaskElementUntilClearance: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to mask elements until clearance."
        },
    )
    MaskElementUntilUnmasking: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to mask elements until unmasking."
        },
    )
    UnmaskElement: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to unmask elements."},
    )
    MaskAlarm: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to mask alarms."},
    )
    AlarmUnmasking: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to unmask alarms."},
    )
    AlarmTakeOwnership: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to take ownership of alarms."
        },
    )
    AccessElement: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to open elements."},
    )
    DataDisplayAccess: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user has access to data pages."},
    )
    ServiceDataDisplayAccess: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user has access to data pages of services."
        },
    )
    AccessAlarms: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to open alarms."},
    )
    ReleaseOwnershipOtherUser: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to release ownership of alarms that are being owned by other users."
        },
    )
    Trending: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user has access to trending."},
    )
    Dashboards: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user has access to DMS Dashboards"},
    )
    Reporter: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user has access to DMS Reporter"},
    )
    Surveyor: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user has access to the Surveyor."},
    )
    TicketsUI: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user has access to DMS Ticketing."},
    )
    TicketsConfigUI: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to configure ticket domains."
        },
    )
    TicketsAddTicket: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to add tickets."},
    )
    TicketsEditTicket: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to edit tickets."},
    )
    TicketsDeleteTicket: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to delete tickets."},
    )
    DashboardsAdd: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to add dashboards."},
    )
    DashboardsEdit: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to edit dashboards."},
    )
    DashboardsDelete: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to delete dashboards."},
    )
    JobsViewAll: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to view all jobs."},
    )
    JobsCreateUpdateJobs: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to create or update jobs."
        },
    )
    JobsDeleteJobs: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to delete jobs."},
    )
    JobsCreateUpdateDeleteSections: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to create, update or delete job sections."
        },
    )
    Collaboration: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to use the collaboration feature."
        },
    )
    ViewNotes: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to view notes."},
    )
    ShareItem: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to share DataMiner items via dataminer.services."
        },
    )
    UnshareItem: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to stop the sharing of DataMiner items via dataminer.services."
        },
    )
    UpdateSharedItems: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to make changes to a share of DataMiner items via dataminer.services."
        },
    )
    SendEmail: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the user is allowed to send emails."},
    )
    MonitoringUI: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to access the Monitoring app."
        },
    )
    UserDefinableAppPublish: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to publish user-defined apps."
        },
    )
    UserDefinableAppEdit: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to edit user-defined apps."
        },
    )
    UserDefinableAppDelete: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to delete user-defined apps."
        },
    )
    UserDefinableAppAdd: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to create user-defined apps."
        },
    )
    UserDefinableAppView: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to view user-defined apps."
        },
    )
    ViewSharedItems: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to view items shared via dataminer.services."
        },
    )
    Security: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to modify security settings."
        },
    )
    SDAutomation: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to open the Automation module in DataMiner Cube and view the list of available Automation scripts in web apps."
        },
    )
    AutomationExecuteScripts: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the user is allowed to execute Automation scripts."
        },
    )
