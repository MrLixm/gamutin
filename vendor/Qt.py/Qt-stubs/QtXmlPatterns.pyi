from typing import overload
import PySide2.QtCore
import shiboken2
import typing
T = typing.TypeVar('T')

class QAbstractMessageHandler(PySide2.QtCore.QObject):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,None] = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def handleMessage(self, type: PySide2.QtCore.QtMsgType, description: str, identifier: PySide2.QtCore.QUrl, sourceLocation: QSourceLocation) -> None: ...
    def message(self, type: PySide2.QtCore.QtMsgType, description: str, identifier: PySide2.QtCore.QUrl = ..., sourceLocation: QSourceLocation = ...) -> None: ...

class QAbstractUriResolver(PySide2.QtCore.QObject):
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject,None] = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def resolve(self, relative: PySide2.QtCore.QUrl, baseURI: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl: ...

class QAbstractXmlNodeModel(shiboken2.Object):
    class NodeCopySetting:
        InheritNamespaces: typing.ClassVar[QAbstractXmlNodeModel.NodeCopySetting] = ...
        PreserveNamespaces: typing.ClassVar[QAbstractXmlNodeModel.NodeCopySetting] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __and__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __rand__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __rmul__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __ror__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __rsub__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __rxor__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __sub__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...
        def __xor__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.NodeCopySetting: ...

    class SimpleAxis:
        FirstChild: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
        NextSibling: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
        Parent: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
        PreviousSibling: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __and__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __rand__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __rmul__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __ror__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __rsub__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __rxor__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __sub__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
        def __xor__(self, other: typing.SupportsInt) -> QAbstractXmlNodeModel.SimpleAxis: ...
    FirstChild: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
    InheritNamespaces: typing.ClassVar[QAbstractXmlNodeModel.NodeCopySetting] = ...
    NextSibling: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
    Parent: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
    PreserveNamespaces: typing.ClassVar[QAbstractXmlNodeModel.NodeCopySetting] = ...
    PreviousSibling: typing.ClassVar[QAbstractXmlNodeModel.SimpleAxis] = ...
    def __init__(self) -> None: ...
    def attributes(self, element: QXmlNodeModelIndex) -> typing.List[QXmlNodeModelIndex]: ...
    def baseUri(self, ni: QXmlNodeModelIndex) -> PySide2.QtCore.QUrl: ...
    def compareOrder(self, ni1: QXmlNodeModelIndex, ni2: QXmlNodeModelIndex) -> QXmlNodeModelIndex.DocumentOrder: ...
    @overload
    def createIndex(self, data: int, additionalData: int) -> QXmlNodeModelIndex: ...
    @overload
    def createIndex(self, pointer: int, additionalData: int = ...) -> QXmlNodeModelIndex: ...
    @overload
    def createIndex(self, data: int) -> QXmlNodeModelIndex: ...
    def documentUri(self, ni: QXmlNodeModelIndex) -> PySide2.QtCore.QUrl: ...
    def elementById(self, NCName: QXmlName) -> QXmlNodeModelIndex: ...
    def isDeepEqual(self, ni1: QXmlNodeModelIndex, ni2: QXmlNodeModelIndex) -> bool: ...
    def kind(self, ni: QXmlNodeModelIndex) -> QXmlNodeModelIndex.NodeKind: ...
    def name(self, ni: QXmlNodeModelIndex) -> QXmlName: ...
    def namespaceBindings(self, n: QXmlNodeModelIndex) -> typing.List[QXmlName]: ...
    def namespaceForPrefix(self, *args, **kwargs) -> typing.Any: ...
    def nextFromSimpleAxis(self, axis: QAbstractXmlNodeModel.SimpleAxis, origin: QXmlNodeModelIndex) -> QXmlNodeModelIndex: ...
    def nodesByIdref(self, NCName: QXmlName) -> typing.List[QXmlNodeModelIndex]: ...
    def root(self, n: QXmlNodeModelIndex) -> QXmlNodeModelIndex: ...
    def sendNamespaces(self, n: QXmlNodeModelIndex, receiver: QAbstractXmlReceiver) -> None: ...
    def sourceLocation(self, index: QXmlNodeModelIndex) -> QSourceLocation: ...
    def stringValue(self, n: QXmlNodeModelIndex) -> str: ...
    def typedValue(self, n: QXmlNodeModelIndex) -> typing.Any: ...

class QAbstractXmlReceiver(shiboken2.Object):
    def __init__(self) -> None: ...
    def atomicValue(self, value: typing.Any) -> None: ...
    def attribute(self, name: QXmlName, value: str) -> None: ...
    def characters(self, value: str) -> None: ...
    def comment(self, value: str) -> None: ...
    def endDocument(self) -> None: ...
    def endElement(self) -> None: ...
    def endOfSequence(self) -> None: ...
    def namespaceBinding(self, name: QXmlName) -> None: ...
    def processingInstruction(self, target: QXmlName, value: str) -> None: ...
    def startDocument(self) -> None: ...
    def startElement(self, name: QXmlName) -> None: ...
    def startOfSequence(self) -> None: ...
    def whitespaceOnly(self, value: str) -> None: ...

class QSourceLocation(shiboken2.Object):
    @overload
    def __init__(self, uri: PySide2.QtCore.QUrl, line: int = ..., column: int = ...) -> None: ...
    @overload
    def __init__(self, other: QSourceLocation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def column(self) -> int: ...
    def isNull(self) -> bool: ...
    def line(self) -> int: ...
    def setColumn(self, newColumn: int) -> None: ...
    def setLine(self, newLine: int) -> None: ...
    def setUri(self, newUri: PySide2.QtCore.QUrl) -> None: ...
    def uri(self) -> PySide2.QtCore.QUrl: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QXmlFormatter(QXmlSerializer):
    def __init__(self, query: QXmlQuery, outputDevice: PySide2.QtCore.QIODevice) -> None: ...
    def atomicValue(self, value: typing.Any) -> None: ...
    def attribute(self, name: QXmlName, value: str) -> None: ...
    def characters(self, value: str) -> None: ...
    def comment(self, value: str) -> None: ...
    def endDocument(self) -> None: ...
    def endElement(self) -> None: ...
    def endOfSequence(self) -> None: ...
    def indentationDepth(self) -> int: ...
    def processingInstruction(self, name: QXmlName, value: str) -> None: ...
    def setIndentationDepth(self, depth: int) -> None: ...
    def startDocument(self) -> None: ...
    def startElement(self, name: QXmlName) -> None: ...
    def startOfSequence(self) -> None: ...

class QXmlItem(shiboken2.Object):
    @overload
    def __init__(self, atomicValue: typing.Any) -> None: ...
    @overload
    def __init__(self, node: QXmlNodeModelIndex) -> None: ...
    @overload
    def __init__(self, other: QXmlItem) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def isAtomicValue(self) -> bool: ...
    def isNode(self) -> bool: ...
    def isNull(self) -> bool: ...
    def toAtomicValue(self) -> typing.Any: ...
    def toNodeModelIndex(self) -> QXmlNodeModelIndex: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QXmlName(shiboken2.Object):
    @overload
    def __init__(self, namePool: QXmlNamePool, localName: str, namespaceURI: str = ..., prefix: str = ...) -> None: ...
    @overload
    def __init__(self, other: QXmlName) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def fromClarkName(cls, clarkName: str, namePool: QXmlNamePool) -> QXmlName: ...
    @classmethod
    def isNCName(cls, candidate: str) -> bool: ...
    def isNull(self) -> bool: ...
    def localName(self, query: QXmlNamePool) -> str: ...
    def namespaceUri(self, query: QXmlNamePool) -> str: ...
    def prefix(self, query: QXmlNamePool) -> str: ...
    def toClarkName(self, query: QXmlNamePool) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QXmlNamePool(shiboken2.Object):
    @overload
    def __init__(self, other: QXmlNamePool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __copy__(self) -> None: ...

class QXmlNodeModelIndex(shiboken2.Object):
    class DocumentOrder:
        Follows: typing.ClassVar[QXmlNodeModelIndex.DocumentOrder] = ...
        Is: typing.ClassVar[QXmlNodeModelIndex.DocumentOrder] = ...
        Precedes: typing.ClassVar[QXmlNodeModelIndex.DocumentOrder] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __and__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __rand__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __rmul__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __ror__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __rsub__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __rxor__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __sub__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...
        def __xor__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.DocumentOrder: ...

    class NodeKind:
        Attribute: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        Comment: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        Document: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        Element: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        Namespace: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        ProcessingInstruction: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        Text: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __and__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __rand__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __rmul__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __ror__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __rsub__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __rxor__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __sub__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
        def __xor__(self, other: typing.SupportsInt) -> QXmlNodeModelIndex.NodeKind: ...
    Attribute: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    Comment: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    Document: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    Element: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    Follows: typing.ClassVar[QXmlNodeModelIndex.DocumentOrder] = ...
    Is: typing.ClassVar[QXmlNodeModelIndex.DocumentOrder] = ...
    Namespace: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    Precedes: typing.ClassVar[QXmlNodeModelIndex.DocumentOrder] = ...
    ProcessingInstruction: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    Text: typing.ClassVar[QXmlNodeModelIndex.NodeKind] = ...
    @overload
    def __init__(self, other: QXmlNodeModelIndex) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def additionalData(self) -> int: ...
    def data(self) -> int: ...
    def internalPointer(self) -> int: ...
    def isNull(self) -> bool: ...
    def model(self) -> QAbstractXmlNodeModel: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QXmlQuery(shiboken2.Object):
    class QueryLanguage:
        XPath20: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
        XQuery10: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
        XSLT20: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
        XmlSchema11IdentityConstraintField: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
        XmlSchema11IdentityConstraintSelector: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __and__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __rand__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __rmul__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __ror__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __rsub__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __rxor__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __sub__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
        def __xor__(self, other: typing.SupportsInt) -> QXmlQuery.QueryLanguage: ...
    XPath20: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
    XQuery10: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
    XSLT20: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
    XmlSchema11IdentityConstraintField: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
    XmlSchema11IdentityConstraintSelector: typing.ClassVar[QXmlQuery.QueryLanguage] = ...
    @overload
    def __init__(self, queryLanguage: QXmlQuery.QueryLanguage, np: QXmlNamePool = ...) -> None: ...
    @overload
    def __init__(self, np: QXmlNamePool) -> None: ...
    @overload
    def __init__(self, other: QXmlQuery) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def bindVariable(self, localName: str, arg__2: PySide2.QtCore.QIODevice) -> None: ...
    @overload
    def bindVariable(self, localName: str, query: QXmlQuery) -> None: ...
    @overload
    def bindVariable(self, localName: str, value: QXmlItem) -> None: ...
    @overload
    def bindVariable(self, name: QXmlName, arg__2: PySide2.QtCore.QIODevice) -> None: ...
    @overload
    def bindVariable(self, name: QXmlName, query: QXmlQuery) -> None: ...
    @overload
    def bindVariable(self, name: QXmlName, value: QXmlItem) -> None: ...
    @overload
    def evaluateTo(self, callback: QAbstractXmlReceiver) -> bool: ...
    @overload
    def evaluateTo(self, result: QXmlResultItems) -> None: ...
    @overload
    def evaluateTo(self, target: PySide2.QtCore.QIODevice) -> bool: ...
    def initialTemplateName(self) -> QXmlName: ...
    def isValid(self) -> bool: ...
    def messageHandler(self) -> QAbstractMessageHandler: ...
    def namePool(self) -> QXmlNamePool: ...
    def queryLanguage(self) -> QXmlQuery.QueryLanguage: ...
    @overload
    def setFocus(self, document: PySide2.QtCore.QIODevice) -> bool: ...
    @overload
    def setFocus(self, documentURI: PySide2.QtCore.QUrl) -> bool: ...
    @overload
    def setFocus(self, focus: str) -> bool: ...
    @overload
    def setFocus(self, item: QXmlItem) -> None: ...
    @overload
    def setInitialTemplateName(self, name: QXmlName) -> None: ...
    @overload
    def setInitialTemplateName(self, name: str) -> None: ...
    def setMessageHandler(self, messageHandler: QAbstractMessageHandler) -> None: ...
    @overload
    def setQuery(self, queryURI: PySide2.QtCore.QUrl, baseURI: PySide2.QtCore.QUrl = ...) -> None: ...
    @overload
    def setQuery(self, sourceCode: PySide2.QtCore.QIODevice, documentURI: PySide2.QtCore.QUrl = ...) -> None: ...
    @overload
    def setQuery(self, sourceCode: str, documentURI: PySide2.QtCore.QUrl = ...) -> None: ...
    def setUriResolver(self, resolver: QAbstractUriResolver) -> None: ...
    def uriResolver(self) -> QAbstractUriResolver: ...
    def __copy__(self) -> None: ...

class QXmlResultItems(shiboken2.Object):
    def __init__(self) -> None: ...
    def current(self) -> QXmlItem: ...
    def hasError(self) -> bool: ...
    def next(self) -> QXmlItem: ...

class QXmlSchema(shiboken2.Object):
    @overload
    def __init__(self, other: QXmlSchema) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def documentUri(self) -> PySide2.QtCore.QUrl: ...
    def isValid(self) -> bool: ...
    @overload
    def load(self, data: typing.Union[PySide2.QtCore.QByteArray,bytes], documentUri: PySide2.QtCore.QUrl = ...) -> bool: ...
    @overload
    def load(self, source: PySide2.QtCore.QIODevice, documentUri: PySide2.QtCore.QUrl = ...) -> bool: ...
    @overload
    def load(self, source: PySide2.QtCore.QUrl) -> bool: ...
    def messageHandler(self) -> QAbstractMessageHandler: ...
    def namePool(self) -> QXmlNamePool: ...
    def setMessageHandler(self, handler: QAbstractMessageHandler) -> None: ...
    def setUriResolver(self, resolver: QAbstractUriResolver) -> None: ...
    def uriResolver(self) -> QAbstractUriResolver: ...

class QXmlSchemaValidator(shiboken2.Object):
    @overload
    def __init__(self, schema: QXmlSchema) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def messageHandler(self) -> QAbstractMessageHandler: ...
    def namePool(self) -> QXmlNamePool: ...
    def schema(self) -> QXmlSchema: ...
    def setMessageHandler(self, handler: QAbstractMessageHandler) -> None: ...
    def setSchema(self, schema: QXmlSchema) -> None: ...
    def setUriResolver(self, resolver: QAbstractUriResolver) -> None: ...
    def uriResolver(self) -> QAbstractUriResolver: ...
    @overload
    def validate(self, data: typing.Union[PySide2.QtCore.QByteArray,bytes], documentUri: PySide2.QtCore.QUrl = ...) -> bool: ...
    @overload
    def validate(self, source: PySide2.QtCore.QIODevice, documentUri: PySide2.QtCore.QUrl = ...) -> bool: ...
    @overload
    def validate(self, source: PySide2.QtCore.QUrl) -> bool: ...

class QXmlSerializer(QAbstractXmlReceiver):
    def __init__(self, query: QXmlQuery, outputDevice: PySide2.QtCore.QIODevice) -> None: ...
    def atomicValue(self, value: typing.Any) -> None: ...
    def attribute(self, name: QXmlName, value: str) -> None: ...
    def characters(self, value: str) -> None: ...
    def codec(self) -> PySide2.QtCore.QTextCodec: ...
    def comment(self, value: str) -> None: ...
    def endDocument(self) -> None: ...
    def endElement(self) -> None: ...
    def endOfSequence(self) -> None: ...
    def namespaceBinding(self, nb: QXmlName) -> None: ...
    def outputDevice(self) -> PySide2.QtCore.QIODevice: ...
    def processingInstruction(self, name: QXmlName, value: str) -> None: ...
    def setCodec(self, codec: PySide2.QtCore.QTextCodec) -> None: ...
    def startDocument(self) -> None: ...
    def startElement(self, name: QXmlName) -> None: ...
    def startOfSequence(self) -> None: ...
