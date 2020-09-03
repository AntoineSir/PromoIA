from azureml.core.run import Run
run = Run.get_context()

def main():
    print("coucou")
    run.log("print", "kikooo")

if __name__ == "__main__":
    main()