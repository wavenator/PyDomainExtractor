import typing
import pydomainextractor.extractor


class DomainExtractor:
    '''
    PyDomainExtractor is a highly optimized Domain Name Extraction library written in C++
    '''
    engine: typing.Optional[pydomainextractor.extractor.DomainExtractor] = None

    def __new__(
        cls,
        suffix_list_data: typing.Optional[str] = None,
    ):
        if suffix_list_data is None:
            if DomainExtractor.engine is None:
                DomainExtractor.engine = pydomainextractor.extractor.DomainExtractor()

            return DomainExtractor.engine
        else:
            return pydomainextractor.extractor.DomainExtractor(suffix_list_data)
