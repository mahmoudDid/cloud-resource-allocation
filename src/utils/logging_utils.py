"""Logging setup utility."""

import logging
import sys


def setup_logger(name: str = "CloudScheduler", level: str = "INFO") -> logging.Logger:
    """Configure a standard logger writing to stdout."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    return logger
