from core.config_loader import ConfigLoader
from generators.banking_data_generator import BankingDataGenerator


def main():

    print("=" * 50)
    print("Enterprise Banking Data Platform")
    print("Data Generation")
    print("=" * 50)

    # ---------------------------------------------------------
    # Load configuration
    # ---------------------------------------------------------
    config = ConfigLoader()
    config.load()

    print("\nProject Configuration")
    print("=" * 50)
    print(config.get_config())

    print("\nGeneration Rules")
    print("=" * 50)
    print(config.get_generation_rules())

    print("\nDQ Rules")
    print("=" * 50)
    print(config.get_dq_rules())

    # ---------------------------------------------------------
    # Read generation configuration
    # ---------------------------------------------------------
    project_config = config.get_config()

    generation_config = project_config["generation"]

    output_directory = generation_config["output_directory"]
    random_seed = generation_config["random_seed"]
    simulation_days = generation_config["simulation_days"]

    # ---------------------------------------------------------
    # Create generator
    # ---------------------------------------------------------
    generator = BankingDataGenerator(
        output_directory=output_directory,
        seed=random_seed
    )

    # ---------------------------------------------------------
    # Generate banking data
    # ---------------------------------------------------------
    generator.generate_branches()
    generator.generate_employees()
    generator.generate_customers()
    generator.generate_accounts()
    generator.generate_loans()
    generator.generate_credit_cards()
    generator.generate_beneficiaries()

    generator.generate_transactions(
        days=simulation_days
    )

    # ---------------------------------------------------------
    # Save generated data
    # ---------------------------------------------------------
    generator.save_data()

    print("\n" + "=" * 50)
    print("DATA GENERATION COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()