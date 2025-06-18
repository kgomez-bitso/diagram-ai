"""Main entry point for the Diagram AI application.

This script demonstrates the creation of a simple AWS infrastructure diagram using the Diagram AI library.
It creates multiple EC2 instances, establishes relationships between them, and renders the diagram.

Example:
    To run this script and generate the diagram:
    $ python main.py

The script will create a diagram showing the following AWS resources:
    - 4 EC2 instances connected in a specific topology
    - Relationships showing the connections between instances
"""

from tree_diagram.nodes.builders.node_builder import NodeBuilder
from tree_diagram.tree import Tree
from diagram_manager.manager import DiagramManager

builder = NodeBuilder()

builder.set_provider("aws")
builder.set_name("EC2 1")
builder.set_id("aws_ec2_1")
builder.set_type("ec2")
first_node = builder.build_node()

builder.reset()

builder.set_provider("aws")
builder.set_name("EC2 2")
builder.set_id("aws_ec2_2")
builder.set_type("ec2")
builder.set_relationship("aws_ec2_1")
second_node = builder.build_node()

builder.reset()

builder.set_provider("aws")
builder.set_name("EC2 3")
builder.set_id("aws_ec2_3")
builder.set_type("ec2")
builder.set_relationship("aws_ec2_2")
third_node = builder.build_node()

builder.reset()

builder.set_provider("aws")
builder.set_name("EC2 4")
builder.set_id("aws_ec2_4")
builder.set_type("ec2")
builder.set_relationship("aws_ec2_2")
builder.set_relationship("aws_ec2_3")
fourth_node = builder.build_node()

tree = Tree()
tree.add_node(first_node)
tree.add_node(fourth_node)
tree.add_node(second_node)
tree.add_node(third_node)

diagram_manager = DiagramManager()
diagram_manager.render("My new diagram", tree)
