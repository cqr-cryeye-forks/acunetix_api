import enum


class ReportTemplateIds(enum.Enum):
    COMPREHENSIVE = '11111111-1111-1111-1111-111111111126'
    DEVELOPER = '11111111-1111-1111-1111-111111111111'
    QUICK = '11111111-1111-1111-1111-111111111112'
    EXECUTIVE_SUMMARY = '11111111-1111-1111-1111-111111111113'
    HIPAA = '11111111-1111-1111-1111-111111111114'
    AFFECTED_ITEMS = '11111111-1111-1111-1111-111111111115'
    SCAN_COMPARISON = '11111111-1111-1111-1111-111111111124'
    CWE_2011 = '11111111-1111-1111-1111-111111111116'
    ISO_27001 = '11111111-1111-1111-1111-111111111117'
    NIST_SP800_53 = '11111111-1111-1111-1111-111111111118'
    OWASP_TOP_10_2013 = '11111111-1111-1111-1111-111111111119'
    OWASP_TOP_10_2017 = '11111111-1111-1111-1111-111111111125'
    PCI_DSS_3_2 = '11111111-1111-1111-1111-111111111120'
    SARBANES_OXLEY = '11111111-1111-1111-1111-111111111121'
    STIG_DISA = '11111111-1111-1111-1111-111111111122'
    WASC_THREAT_CLASSIFICATION = '11111111-1111-1111-1111-111111111123'


class ProfileIds(enum.Enum):
    FULL_SCAN = '11111111-1111-1111-1111-111111111111'
    HIGH_RISK_VULNERABILITIES = '11111111-1111-1111-1111-111111111112'
    CROSS_SITE_SCRIPTING_VULNERABILITIES = '11111111-1111-1111-1111-111111111116'
    SQL_INJECTION_VULNERABILITIES = '11111111-1111-1111-1111-111111111113'
    WEAK_PASSWORDS = '11111111-1111-1111-1111-111111111115'
    CRAWL_ONLY = '11111111-1111-1111-1111-111111111117'


class ExportTypes(enum.Enum):
    JSON = '21111111-1111-1111-1111-111111111130'
    CSV_LOCATIONS = '21111111-1111-1111-1111-111111111140'
    CSV_VULNERABILITIES = '21111111-1111-1111-1111-111111111141'
    XML = '21111111-1111-1111-1111-111111111111'


DEFAULT_REPORT_TEMPLATE_ID = ReportTemplateIds.COMPREHENSIVE.value
DEFAULT_PROFILE_ID = ProfileIds.FULL_SCAN.value
