from fdce.__version__ import __version__

try:
    from fdce._extension._fdce import get_coeff
    from fdce._extension._fdce import derivate
except ImportError:
    from fdce.get_coeff import get_coeff
    from fdce.derivate import derivate

__all__ = ["get_coeff"]
