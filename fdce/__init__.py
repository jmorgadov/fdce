try:
    from fdce._extension._fdce import derivate, get_coeff
except ImportError:
    from fdce.derivate import derivate
    from fdce.get_coeff import get_coeff

__version__ = '0.1.1'
__all__ = ["get_coeff"]
