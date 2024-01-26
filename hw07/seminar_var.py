from os import chdir
from pathlib import Path


def sort_files(path: Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)

    if groups is None:
        groups = {
            Path('video'): ['avi', 'mkv'],
            Path('image'): ['jpg', 'png'],
            ...
        }

    reverse_groups = {}
    for target_dir, extension_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for extension in extension_list:
            reverse_groups[f'.{extension}'] = target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups.keys():
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    sort_files(Path('C:/Users/new_dir/target/'))
