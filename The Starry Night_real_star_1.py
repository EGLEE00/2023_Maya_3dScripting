import maya.cmds as cmds
import functools

def createUI( pWindowTitle, pApplyCallback) :
    windowID = 'myWindowID'

    if cmds.window(windowID, exists=True) :
        cmds.deleteUI(windowID)

    cmds.window(windowID, title=pWindowTitle, sizeavle=False, resizeToFitChildren=True)

    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1,75), (2,60), (3,60)], columnOffset=[(1,'right',3)])

    cmds.text(label='Time Range:')

    startTimeField = cmds.intField(value = cmds.playbackOptions(q=True, minTime=True))

    endTimeField = cmds.intField(value = cmds.playbackOptions(q=True, maxTime=True))

    cmds.text(label='Attribute:')

    targetAttributeField = cmds.textField(text='rotateY')

    cmds.separator(h=10, style='none')

    cmds.separator(h=10, style='none')
    cmds.separator(h=10, style='none')
    cmds.separator(h=10, style='none')

    cmds.separator(h=10, style='none')

    cmds.button( label='Apply', command=functools.partial ( pApplyCallback,
                                                            startTimeField,
                                                            endTimeField,
                                                            targetAttributeField ))

    def cancelCallback( *pArgs ) :
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )

    cmds.button( label='Cancel', command=cancelCallback )

    cmds.showWindow()

def applyCallback( pStartTimeField, pEndTimeField, pTargetAttributeField, *pArgs ):

    # print 'Apply button pressed.'

    startTime = cmds.intField( pStartTimeField, query=True, value=True )
    endTime = cmds.intField( pEndTimeField, query=True, value=True )
    targetAttribute = cmds.textField( pTargetAttributeField, query=True, text=True )

    print 'Start Time: %s' % ( startTime )
    print 'End Time: %s' % ( endTime )
    print 'Attribute: %s' % ( targetAttribute ) 

createUI( 'My Title', applyCallback )
