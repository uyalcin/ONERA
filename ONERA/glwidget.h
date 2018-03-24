#ifndef GLWIDGET_H
#define GLWIDGET_H

#include <QGLWidget>
#include <GL/gl.h>
#include <GL/glu.h>
#include <vector>
#include "box.h"

struct color
{
    int r;
    int g;
    int b;
    int a;
};

class GLWidget : public QGLWidget
{
    Q_OBJECT
public:
    explicit GLWidget(QWidget *parent = 0);

    void initializeGL();
    void paintGL();
    void resizeGL(int w, int h);

    // Draw a Cube
    void drawCube(float x, float y, float z, float w, float h, float l, color c);

    int nbBoxs() { return boxs.size(); }

private:
    std::vector<color> colors;
    std::vector<Box> boxs;
    int state;

public slots:
    void nextState();
    void previousState();
    void finalState();
    void startState();
};

#endif // GLWIDGET_H

