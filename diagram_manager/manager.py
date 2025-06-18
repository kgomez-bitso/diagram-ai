"""Module for rendering infrastructure diagrams from node trees.

This module provides functionality to visualize infrastructure as code by converting
a tree of nodes into a graphical diagram using the diagrams library.
"""

from diagrams import Diagram
from tree_diagram.tree import Tree

class DiagramManager:
    """Handles the rendering of infrastructure diagrams from a tree of nodes.
    
    This class provides methods to convert a tree of node objects into a visual
    representation using the diagrams library.
    """
    
    def render(self, diagram_name: str, tree: Tree) -> None:
        """Render a diagram from a tree of nodes.
        
        Args:
            diagram_name: The title/name of the output diagram
            tree: A Tree object containing the nodes to be rendered
            
        The method performs the following steps:
            1. Creates a new diagram with the specified name
            2. Creates a mapping of node IDs to their diagram elements
            3. Establishes relationships between nodes using the '>>' operator
            
        Note:
            The diagram is saved as a PNG file with the same name as diagram_name.
            The diagram is not displayed by default (show=False).
        """
        # Create a new diagram context
        with Diagram(diagram_name, show=False):
            # First pass: create all elements
            elements = {}
            for node in tree.get_all_nodes():
                elements[node.get_id()] = node.get_element()
            
            # Second pass: establish relationships
            for node in tree.get_all_nodes():
                if node.get_relationships():
                    element = elements[node.get_id()]
                    for relationship in node.get_relationships():
                        # Use the '>>' operator to create a relationship in the diagram
                        element >> elements[relationship]
                else:
                    elements[node.get_id()]