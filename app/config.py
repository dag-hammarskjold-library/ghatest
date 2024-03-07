class ProductionConfig(object):
    CRED = "Production Credential 2"
    FOO = "bar"
    DEBUG = False
    TESTING = False
class DevelopmentConfig(ProductionConfig):
    CRED = "Development Credential"
    FOO = "baz"
    DEBUG = True
    TESTING = False
class AcceptanceTestingConfig(ProductionConfig):
    CRED = "QAT/UAT Credential"
    DEBUG = True
    TESTING = False
class TestingConfig(ProductionConfig):
    CRED = "Testing Credential"
    DEBUG = True
    TESTING = True

def Config(which):
    if which == "prod":
        return ProductionConfig
    elif which == "dev":
        return DevelopmentConfig
    elif which == "qat":
        return AcceptanceTestingConfig
    elif which == "test":
        return TestingConfig
    else:
        return DevelopmentConfig