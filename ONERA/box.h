#ifndef BOX_H
#define BOX_H

#include "vector3.h"
#include <QString>
#include <QStringList>

class Box
{
public:
    Box(Vector3 _dimension);
    Box(QString _box_string);
    Vector3 getPosition();
    Vector3 getDimension();
    void setPosition(Vector3 _position);
private:

    Vector3 dimension;
    Vector3 position;
    friend std::ostream& operator<<(std::ostream& out, const Box &b);
};

#endif // BOX_H
