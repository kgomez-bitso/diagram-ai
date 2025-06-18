from diagrams.aws.compute import EC2
from typing import Any
from tree_diagram.nodes.types.node import Node

class AwsNode(Node):
    """A concrete implementation of Node for AWS resources.
    
    This class provides AWS-specific node functionality and uses the diagrams library
    to generate appropriate visual representations of AWS resources.
    """
    
    def __init__(self) -> None:
        """Initialize a new AwsNode instance with default values."""
        self.element: any = None
        self.name: str = ""
        self.id: str = ""
        self.type: str = ""
        self.relationships: list[str] = []

    def reset(self) -> None:
        """Reset the node to its initial state.
        
        Clears all attributes including element, name, id, type, and relationships.
        """
        self.element = None
        self.name = ""
        self.id = ""
        self.type = ""
        self.relationships = []

    def set_name(self, name: str) -> None:
        """Set the name of the AWS node.
        
        Args:
            name: The name to assign to this AWS resource
        """
        self.name = name    

    def set_id(self, id: str) -> None:
        """Set a unique identifier for the AWS node.
        
        Args:
            id: A unique string identifier for this AWS resource
        """
        self.id = id

    def set_type(self, type: str) -> None:
        """Set the type of the AWS resource.
        
        Args:
            type: The AWS resource type (e.g., 'ec2', 's3')
        """
        self.type = type

    def set_relationship(self, relationship: str) -> None:
        """Add a relationship to another node.
        
        Args:
            relationship: A string describing the relationship to another AWS resource
        """
        self.relationships.append(relationship)

    def get_element(self) -> Any:
        """Get the diagrams library element for this AWS resource.
        
        Returns:
            Any: A diagrams.aws.* instance corresponding to the node type
            
        Note:
            Currently only supports 'ec2' type. Returns None for unsupported types.
        """
        if self.type == "ec2":
            return EC2(self.name)

    def get_name(self) -> str:
        """Get the name of the AWS node.
        
        Returns:
            str: The name of the AWS resource
        """
        return self.name

    def get_id(self) -> str:
        """Get the unique identifier of the AWS node.
        
        Returns:
            str: The unique identifier of the AWS resource
        """
        return self.id

    def get_type(self) -> str:
        """Get the type of the AWS resource.
        
        Returns:
            str: The type of the AWS resource (e.g., 'ec2')
        """
        return self.type

    def get_relationships(self) -> list[str]:
        """Get all relationships defined for this node.
        
        Returns:
            list[str]: A list of relationship descriptions
        """
        return self.relationships