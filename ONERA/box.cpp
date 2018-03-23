#include "box.h"

Box::Box(Vector3 _dimension): dimension(_dimension)
{
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
