# coding: utf-8

"""
    trieve-server

    Trieve REST API OpenAPI Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SearchCollectionsData(BaseModel):
    """
    SearchCollectionsData
    """ # noqa: E501
    collection_id: StrictStr = Field(description="Collection_id specifies the collection to search within. Results will only consist of chunks which are bookmarks within the specified collection.")
    date_bias: Optional[StrictBool] = Field(default=None, description="Set date_bias to true to bias search results towards more recent chunks. This will work best in hybrid search mode.")
    filters: Optional[Any] = Field(default=None, description="Filters is a JSON object which can be used to filter chunks. The values on each key in the object will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata.")
    link: Optional[List[StrictStr]] = Field(default=None, description="The link set is a comma separated list of links. This can be used to filter chunks by link. HNSW indices do not exist for links, so there is a performance hit for filtering on them.")
    page: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon.")
    query: StrictStr = Field(description="The query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set.")
    search_type: StrictStr = Field(description="Search_type can be either \"semantic\", \"fulltext\", or \"hybrid\". \"hybrid\" will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \"semantic\" will pull in one page (10 chunks) of the nearest cosine distant vectors. \"fulltext\" will pull in one page (10 chunks) of full-text results based on SPLADE.")
    tag_set: Optional[List[StrictStr]] = Field(default=None, description="The tag set is a comma separated list of tags. This can be used to filter chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit for filtering on them.")
    __properties: ClassVar[List[str]] = ["collection_id", "date_bias", "filters", "link", "page", "query", "search_type", "tag_set"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchCollectionsData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if date_bias (nullable) is None
        # and model_fields_set contains the field
        if self.date_bias is None and "date_bias" in self.model_fields_set:
            _dict['date_bias'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if tag_set (nullable) is None
        # and model_fields_set contains the field
        if self.tag_set is None and "tag_set" in self.model_fields_set:
            _dict['tag_set'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchCollectionsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collection_id": obj.get("collection_id"),
            "date_bias": obj.get("date_bias"),
            "filters": obj.get("filters"),
            "link": obj.get("link"),
            "page": obj.get("page"),
            "query": obj.get("query"),
            "search_type": obj.get("search_type"),
            "tag_set": obj.get("tag_set")
        })
        return _obj

