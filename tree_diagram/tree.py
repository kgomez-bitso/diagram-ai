from tree_diagram.nodes.types.node import Node

class Tree:
    """A class representing a tree structure for managing nodes.
    
    This class provides functionality to manage a collection of nodes in a tree-like
    structure where each node is accessible by its unique identifier.
    """

    tree: dict[str, Node] = {}

    def __init__(self) -> None:
        """Initialize a new Tree instance with an empty node dictionary."""
        pass

    def add_node(self, node: Node) -> None:
        """Add a node to the tree.
        
        Args:
            node: The node to add to the tree
            
        Note:
            The node's ID must be unique. If a node with the same ID already exists,
            it will be overwritten.
        """
        self.tree[node.get_id()] = node

    def remove_node(self, node: Node) -> None:
        """Remove a node from the tree.
        
        Args:
            node: The node to remove from the tree
            
        Raises:
            KeyError: If the node's ID is not found in the tree
        """
        del self.tree[node.get_id()]

    def get_node(self, id: str) -> Node:
        """Retrieve a node by its ID.
        
        Args:
            id: The unique identifier of the node to retrieve
            
        Returns:
            Node: The node with the specified ID
            
        Raises:
            KeyError: If no node with the specified ID exists
        """
        return self.tree[id]

    def get_tree(self) -> dict[str, Node]:
        """Get the entire tree structure.
        
        Returns:
            dict[str, Node]: A dictionary mapping node IDs to node instances
        """
        return self.tree

    def clear(self) -> None:
        """Remove all nodes from the tree.
        
        This resets the tree to its initial empty state.
        """
        self.tree = {}

    def get_all_nodes(self) -> list[Node]:
        """Get a list of all nodes in the tree.
        
        Returns:
            list[Node]: A list containing all node instances in the tree
        """
        return list(self.tree.values())

    def update_node(self, id: str, node: Node) -> None:
        """Update a node in the tree.
        
        Args:
            id: The ID of the node to update
            node: The new node instance
            
        Note:
            If no node with the specified ID exists, it will be added to the tree.
        """
        self.tree[id] = node
        