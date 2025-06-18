from tree_diagram.nodes.types.node import Node
from tree_diagram.nodes.types.aws_node import AwsNode

class NodeBuilder:
    """A builder class for creating and configuring Node objects with a specific provider."""
    
    def set_provider(self, provider: str) -> None:
        """Set the cloud provider for the node being built.
        
        Args:
            provider: The cloud provider name (e.g., 'aws')
            
        Raises:
            ValueError: If the provider is not supported
        """
        if provider == "aws":
            self.provider = provider
            self.node = AwsNode()
        else:
            raise ValueError("Provider not supported")

    def set_name(self, name: str) -> None:
        """Set the name of the node.
        
        Args:
            name: The name to assign to the node
            
        Note:
            Provider must be set before calling this method
        """
        if self.__is_provider_set():
            self.node.set_name(name)

    def set_id(self, id: str) -> None:
        """Set the unique identifier for the node.
        
        Args:
            id: The unique identifier for the node
            
        Note:
            Provider must be set before calling this method
        """
        if self.__is_provider_set():
            self.node.set_id(id)

    def set_type(self, type: str) -> None:
        """Set the type of the node (e.g., 'ec2', 's3').
        
        Args:
            type: The type of the node
            
        Note:
            Provider must be set before calling this method
        """
        if self.__is_provider_set():
            self.node.set_type(type)

    def set_description(self, description: str) -> None:
        """Set a description for the node.
        
        Args:
            description: The description text for the node
            
        Note:
            Provider must be set before calling this method
        """
        if self.__is_provider_set():
            self.node.set_description(description)

    def set_relationship(self, relationship: str) -> None:
        """Define relationships between this node and other nodes.
        
        Args:
            relationship: Description of the relationship to other nodes
            
        Note:
            Provider must be set before calling this method
        """
        if self.__is_provider_set():
            self.node.set_relationship(relationship)

    def build_node(self) -> Node:
        """Construct and return the configured node.
        
        Returns:
            Node: The fully configured node instance
            
        Note:
            The builder can be reused after calling this method by calling reset()
        """
        return self.node

    def reset(self) -> None:
        """Reset the builder to its initial state.
        
        This clears the current node and provider, allowing the builder
        to be reused for creating new nodes.
        """
        self.provider = ""
        self.node = None

    def __is_provider_set(self) -> bool:
        """Check if a provider has been set for the builder.
        
        Returns:
            bool: True if provider is set, raises ValueError otherwise
            
        Raises:
            ValueError: If no provider has been set
        """
        if self.provider == "":
            raise ValueError("Provider not set")
        return True