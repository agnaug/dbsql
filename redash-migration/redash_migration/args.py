# Standard Library
import argparse
from dataclasses import dataclass, field

# Third Party
from simple_parsing import ArgumentParser


@dataclass
class RedashCreds:
    redash_url: str  # Redash Workspace URL
    redash_token: str  # Redash Access Token


@dataclass
class DatabricksCreds:
    databricks_workspace: str  # Databricks Workspace URL
    databricks_warehouse: str  # Databricks SQL Warehouse Host


@dataclass
class StorageCreds:
    storage_bucket: str  # S3 Storage Bucket Name
    storage_prefix: str  # S3 Storage Prefix
    storage_path: str = field(init=False)  # Output path to store Redash objects

    def __post_init__(self):
        self.storage_path = f"""{self.storage_bucket.rstrip("/")}/{self.storage_prefix}"""


def parse_args() -> argparse.Namespace:
    parser = ArgumentParser()
    parser.add_arguments(RedashCreds, dest="redash")
    parser.add_arguments(DatabricksCreds, dest="dbx")
    parser.add_arguments(StorageCreds, dest="s3")

    known_args, _ = parser.parse_known_args()

    return known_args
