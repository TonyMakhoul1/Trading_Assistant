from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()


def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    # we give the input to the crew as a dictionnary
    # stock_crew.kickoff, we initiate the crew, it pass the input data
    return result


if __name__ == "__main__":
    run("TESLA")
