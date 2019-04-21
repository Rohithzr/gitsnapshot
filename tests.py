import unittest
from tempfile import mkdtemp
from shutil import rmtree
from pathlib import Path

from gitsnapshot import load_repo


class TestGitSnapshot(unittest.TestCase):
    TEST_REPO_URL = 'https://github.com/kirillsulim/gitsnapshot-integration-test-repo'
    INITIAL_COMMIT_HASH = '985bfc32a4cdb46a638aa2b047d8875323639241'
    TEST_COMMIT_HASH = '18203b63d9fcd742f752371be2415dc22ed7c517'

    def test_load_by_branch(self):
        with TempDirectory() as repo_dir:
            error = load_repo(repo_dir, self.TEST_REPO_URL, branch='master')
            self.assertIsNone(error, 'Error occurred on loading repo')

            file_content = Path(repo_dir).joinpath('file').read_text().strip('\n ')
            self.assertEqual('branch', file_content)

    def test_load_by_tag(self):
        with TempDirectory() as repo_dir:
            error = load_repo(repo_dir, self.TEST_REPO_URL, tag='tagName')
            self.assertIsNone(error, 'Error occurred on loading repo')

            file_content = Path(repo_dir).joinpath('file').read_text().strip('\n ')
            self.assertEqual('tag', file_content)

    def test_load_by_commit(self):
        with TempDirectory() as repo_dir:
            error = load_repo(repo_dir, self.TEST_REPO_URL, commit=self.TEST_COMMIT_HASH)
            self.assertIsNone(error, 'Error occurred on loading repo')

            file_content = Path(repo_dir).joinpath('file').read_text().strip('\n ')
            self.assertEqual('commit', file_content)

    def test_checkout_existing_by_branch(self):
        with TempDirectory() as repo_dir:
            error = load_repo(repo_dir, self.TEST_REPO_URL, commit=self.INITIAL_COMMIT_HASH)
            self.assertIsNone(error, 'Error occurred on loading repo')

            error = load_repo(repo_dir, self.TEST_REPO_URL, branch='master', use_existing=True)
            self.assertIsNone(error, 'Error occurred on loading repo')

            file_content = Path(repo_dir).joinpath('file').read_text().strip('\n ')
            self.assertEqual('branch', file_content)

    def test_checkout_existing_by_tag(self):
        with TempDirectory() as repo_dir:
            error = load_repo(repo_dir, self.TEST_REPO_URL, commit=self.INITIAL_COMMIT_HASH)
            self.assertIsNone(error, 'Error occurred on loading repo')

            error = load_repo(repo_dir, self.TEST_REPO_URL, tag='tagName', use_existing=True)
            self.assertIsNone(error, 'Error occurred on loading repo')

            file_content = Path(repo_dir).joinpath('file').read_text().strip('\n ')
            self.assertEqual('tag', file_content)

    def test_checkout_existing_by_commit(self):
        with TempDirectory() as repo_dir:
            error = load_repo(repo_dir, self.TEST_REPO_URL, commit=self.INITIAL_COMMIT_HASH)
            self.assertIsNone(error, 'Error occurred on loading repo')

            error = load_repo(repo_dir, self.TEST_REPO_URL, commit=self.TEST_COMMIT_HASH, use_existing=True)
            self.assertIsNone(error, 'Error occurred on loading repo')

            file_content = Path(repo_dir).joinpath('file').read_text().strip('\n ')
            self.assertEqual('commit', file_content)


class TempDirectory:
    def __init__(self, clean=True):
        self.dir = None
        self.clean = clean

    def __enter__(self):
        self.dir = mkdtemp()
        return self.dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.clean:
            rmtree(self.dir, ignore_errors=True)
