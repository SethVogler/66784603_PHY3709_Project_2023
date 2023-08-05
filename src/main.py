if __name__ == "__main__":
    try:
        E = find_energy()
        plot_results(E)
    except Exception as e:
        print(f"An error occurred: {e}")
