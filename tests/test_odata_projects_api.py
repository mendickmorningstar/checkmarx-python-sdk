from CheckmarxPythonSDK.CxRestAPISDK import (ProjectsAPI, ScansAPI)
from CheckmarxPythonSDK.CxODataApiSDK import ProjectsODataAPI

project_name = "jvl_git"
scans_api = ScansAPI()
projects_api = ProjectsAPI()
project_id = projects_api.get_project_id_by_project_name_and_team_full_name(project_name=project_name)


def test_top_n_projects_by_risk_score():
    project_odata_api = ProjectsODataAPI()

    number_of_projects = 10
    r = project_odata_api.top_n_projects_by_risk_score(number_of_projects=number_of_projects)

    assert r is not None


def test_top_n_projects_by_last_scan_duration():
    project_odata_api = ProjectsODataAPI()

    number_of_projects = 10
    r = project_odata_api.top_n_projects_by_last_scan_duration(number_of_projects=number_of_projects)

    assert r is not None
