try:
    from fdce._extension._fdce import derivative, get_coeff
except ImportError:
    from fdce.derivate import derivative
    from fdce.get_coeff import get_coeff

__version__ = '0.1.2a1'
__all__ = ["get_coeff"]
