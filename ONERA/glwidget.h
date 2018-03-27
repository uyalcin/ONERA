#ifndef GLWIDGET_H
#define GLWIDGET_H

#include <QGLWidget>
#include <GL/gl.h>
#include <GL/glu.h>
#include <vector>
#include "box.h"
#include "renderwindow.h"
#include <sstream>
#include <QKeyEvent>

struct color
{
    float r;
    float g;
    float b;
    float a;
};

class GLWidget : public QGLWidget
{
    Q_OBJECT
public:
    explicit GLWidget(QWidget *parent = 0);
    void init(std::vector<Box> boxs);

    void initializeGL();
    void paintGL();
    void resizeGL(int w, int h);

    // Draw a Cube
    void drawCube(float x, float y, float z, float w, float h, float l, color c);

    int nbBoxs() { return boxs.size(); }
    void setDataSet(std::vector<Box> boxs);


private:
    std::vector<color> colors;
    std::vector<Box> boxs;
    int state;
    void keyPressEvent(QKeyEvent *);
    float zoom;

public slots:
    void nextState();
    void previousState();
    void finalState();
    void startState();
};

#endif // GLWIDGET_H

