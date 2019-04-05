import abc

class DITKModel(abc.ABC):
    # Any shared data strcutures or methods should be defined as part of the parent class.
    # A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.
    # The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group.

    @classmethod
    @abc.abstractmethod
    def read_dataset(file_names:list, url_names: list, split_ratio: tuple) -> list:
        pass

    @classmethod
    @abc.abstractmethod
    def train(train_set: list) -> Model:
        pass

    # Output
    # format: entity_name, wikipedia_url, geolocation_url, boundary
    @classmethod
    @abc.abstractmethod
    def predict(model: Model, test_set: list) -> list:
        pass

    @classmethod
    @abc.abstractmethod
    def evaluate(model: Model, eval_set: list, eval_func: function) -> dict:
        Pass





