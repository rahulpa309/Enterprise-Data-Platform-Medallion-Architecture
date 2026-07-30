from core.config_loader import ConfigLoader


def main():

    loader = ConfigLoader()

    loader.load()

    print("=" * 50)
    print("Project Configuration")
    print("=" * 50)

    print(loader.get_config())

    print()

    print("=" * 50)
    print("Generation Rules")
    print("=" * 50)

    print(loader.get_generation_rules())

    print()

    print("=" * 50)
    print("DQ Rules")
    print("=" * 50)

    print(loader.get_dq_rules())


if __name__ == "__main__":
    main()