#include "box.h"

Box::Box(Vector3 _dimension): dimension(_dimension)
{
}

Box::Box(QString _box_string)
{
    QStringList list = _box_string.split(",");
    int x1 = list.at(0).toInt();
    int y1 = list.at(1).toInt();
    int z1 = list.at(2).toInt();
    int x2 = list.at(3).toInt();
    int y2 = list.at(4).toInt();
    int z2 = list.at(5).toInt();
    position = Vector3(x1, y1, z1);
    dimension = Vector3(x2-x1, y2-y1, z2-z1);
}

Vector3 Box::getDimension()
{
    return dimension;
}

Vector3 Box::getPosition()
{
    return position;
}

void Box::setPosition(Vector3 _position)
{
    position = _position;
}

std::ostream& operator<<(std::ostream& out, const Box &b)
{
    out << "Position : " << b.position << ", Dimension : " << b.dimension;
    return out;
}

