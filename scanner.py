"""Σάρωση barcode με τον επίσημο σαρωτή της Google (μόνο Android, μέσω της Java κλάσης org.poiotita.Scanner)."""
from kivy.utils import platform

IS_ANDROID = platform == "android"


def available():
    return IS_ANDROID


def start():
    from jnius import autoclass
    S = autoclass("org.poiotita.Scanner")
    act = autoclass("org.kivy.android.PythonActivity").mActivity
    S.scan(act)


def poll():
    """(σε εξέλιξη, αποτέλεσμα, σφάλμα)"""
    from jnius import autoclass
    S = autoclass("org.poiotita.Scanner")
    return bool(S.busy), S.result, S.error
