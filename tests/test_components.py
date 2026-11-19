from src.core.forecaster_2037 import Forecaster2037
from src.security.sovereignty_shield import SovereigntyShield


def test_forecaster_requires_demo_sovereignty_check():
    forecaster = Forecaster2037()
    assert forecaster.predict_threats() is None


def test_forecaster_returns_all_demo_threat_categories():
    forecaster = Forecaster2037()
    forecaster.sovereign_check = lambda: True
    assert forecaster.sovereign_check() is True
    results = forecaster.predict_threats()
    assert len(results) == 4
    assert all(0 <= item["probability"] <= 1 for item in results)


def test_shield_round_trips_base64_demo_encoding():
    shield = SovereigntyShield()
    original = "dados de teste"
    encoded = shield.encrypt_critical_data(original)
    assert "BASE64-DEMO-NOT-ENCRYPTION" in encoded
    assert shield.decrypt_critical_data(encoded) == original


def test_shield_rejects_unknown_format():
    shield = SovereigntyShield()
    try:
        shield.decrypt_critical_data("not-an-encoded-payload")
    except ValueError:
        return
    raise AssertionError("Formato desconhecido deveria ser rejeitado")
