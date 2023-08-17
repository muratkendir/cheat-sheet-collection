# SDO_GEOMETRY Cheatsheet

SDO_GEOMETRY is the data type stores geometries on OracleDB Spatial package.

Main structure of the SDO_GEOMETRY object is like below:
```yaml
SDO_GEOMETRY
  - SDO_GTYPE
  - SDO_SRID
  - SDO_POINT
    - SDO_POINT_TYPE
  - SDO_ELEM_INFO_ARRAY
    - SDO_STARTING_OFFSET
    - SDO_ETYPE
    - SDO_INTERPRETATION
  - SDO_ORDINATES 
```

## Table of SDO_GEOMETRY elements

 **Level** | **Relevant Object** | **Rule(z)** | **Note** 
---|---|---|---
 0 | SDO_GEOMETRY | includes SDO_GTYPE, SDO_SRID, SDO_POINT, SDO_ELEM_INFO_ARRAY, SDO_ORDINATES |  
 1 | SDO_GTYPE | XXXX: First digit stands for Dimension | 2,3,4 
 | XXXX: Second digit stands for linear referencing (measure) system | 0, 3 (X,Y,M), 4 (X,Y,Z,M) |  
 | XXXX: last 2 digits stands for geometry types | 01: Point, 02: Line/Curve, 03: Polygon/Surface, 07:Multipolygon, 08:Solid, 09: MultiSolid |  
 1 | SDO_SRID | SRID code of CRS |  
 1 | SDO_POINT | This object used if SDO_ELEM_INFO and SDO_ORDINATES is NULL | In other words, if only points are stored (not with Linear Referencing and as oriented point). 
 1 | SDO_ELEM_INFO_ARRAY | includes SDO_STARTING_OFFSET, SDO_ETYPE and SDO_INTERPRETATION |  
 2 | SDO_STARTING_OFFSET | Offset in ordinates |  
 2 | SDO_ETYPE | Codes for geometry types | 1003: Exterior (CCW) Simple Polygon, 2003: Interior (CW) Simple Polygon, 1005: Exterior Compound Polygon (w ring), 2005: Interior Compound Polygon (w ring), 1006: Exterior Surface (contains at least 1 polygon), 2006: Interior Surface, 1007: Solid 
 2 | SDO_INTERPRETATION | If the geometry is compound than it specifies how many triplets are part of the geometry. |  
 1 | SDO_ORDINATES | lists and represents the order of the ordinates | X, Y, Z, M 


