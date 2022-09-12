from typing import List, Set

from ..ast_node import AstNode, NodeWriter, ReferenceResolver
from ..code_writer import CodeWriter
from ..function import FunctionParameter
from ..reference import Reference


class ClassConstructor(AstNode):
    parameters: List[FunctionParameter]
    body: CodeWriter

    def __init__(self, parameters: List[FunctionParameter], body: CodeWriter):
        self.parameters = parameters
        self.body = body

    def get_references(self) -> Set[Reference]:
        references: Set[Reference] = set()
        for parameter in self.parameters:
            references = references.union(parameter.get_references())
        references = references.union(self.body.get_references())
        return references

    def write(self, writer: NodeWriter, reference_resolver: ReferenceResolver) -> None:
        writer.write("def __init__(self, ")
        for i, parameter in enumerate(self.parameters):
            writer.write_node(parameter)
            if i < len(self.parameters) - 1:
                writer.write(", ")
        writer.write("):")

        with writer.indent():
            self.body.write(writer=writer, reference_resolver=reference_resolver)