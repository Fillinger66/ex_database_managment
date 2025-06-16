"""
  Copyright (c) 2025 Alexandre Kavadias 

  This project is licensed under the Educational and Non-Commercial Use License.
  See the LICENSE file for details.
"""
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

# TypeVar to represent the entity type that this repository will handle
T = TypeVar('T')

class IRepository(ABC, Generic[T]):
    """
    Abstract Base Class (Interface) for a generic Repository.
    Defines the common CRUD (Create, Read, Update, Delete) operations
    that apply to any aggregate root or entity type.
    """

    @abstractmethod
    def add(self, entity: T) -> Optional[int]:
        """
        Adds a new entity to the repository.
        The entity object's ID should be updated if the operation is successful.
        :param entity: The entity domain object to add.
        :return: The ID of the newly added entity, or None if insertion failed.
        """
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]:
        """
        Retrieves an entity by its ID.
        :param entity_id: The ID of the entity.
        :return: The entity domain object if found, otherwise None.
        """
        pass

    @abstractmethod
    def update(self, entity: T) -> bool:
        """
        Updates an existing entity's information.
        :param entity: The entity domain object with updated information.
        :return: True if the entity was updated, False otherwise.
        """
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        """
        Deletes an entity by its ID.
        :param entity_id: The ID of the entity to delete.
        :return: True if the entity was deleted, False otherwise.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """
        Retrieves all entities of this type.
        :return: A list of entity domain objects.
        """
        pass