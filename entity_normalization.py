import your_module_class

class EntityNormalization(your_module_class.Your_Model_Class):
    # Any shared data strcutures or methods should be defined as part of the parent class.
    # A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.
    # The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group.

    @classmethod
    @abc.abstractmethod
    def read_dataset(self, file_names: list, url_names: list, split_ratio: tuple) -> list:
        '''
        :param file_names: a list of input file names (optional)
        :param url_names: a list of input url_names (optional)
        :param split_ratio: (train_ratio, validation_ration, test_ratio)
        :return: train_data, valid_data, test_data
        '''
        pass

    @classmethod
    @abc.abstractmethod
    def train(self, train_set: list) -> Model:
        '''
        :param train_set: a list of train data
        :return: a model trained on train_set
        '''
        pass

    # Output
    # format: entity_name, wikipedia_url, geolocation_url, boundary
    @classmethod
    @abc.abstractmethod
    def predict(self, model: Model, test_set: list) -> list:
        '''
        :param model: an object of Model Class
        :param test_set: a list of test data
        :return: a list of prediction, each with the format (entity_name, wikipedia_url, geolocation_url, boundary)
        '''
        pass

    @classmethod
    @abc.abstractmethod
    def evaluate(self, model: Model, eval_set: list) -> tuple:
        '''
        :param model: an object of Model Class
        :param eval_set: a list of test data
        :return: (precision, recall, f1 score)
        '''
        Pass





