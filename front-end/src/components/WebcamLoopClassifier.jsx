import React from 'react';
import { Card, Image } from 'semantic-ui-react'
import { Form } from 'semantic-ui-react'

import Webcam from 'react-webcam';


class WebcamLoopClassifer extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      isRecording: false,
      bestLabel: '',
      bestLabelScore: 0,
      imageDataUrl: '',
    }

    this.webcamRef = React.createRef()

    this.videoConstraints = {
      width: props.imageWidth,
      height: props.imageHeight,
      facingMode: "user"
    };
  }

  toggleRecording = async(e) => {
    const desiredRecordingState = !this.state.isRecording;
    this.setState({isRecording: desiredRecordingState})

    if (desiredRecordingState) {
      setTimeout( () => { this.classifyLoop() }, 0) // schedule this work on the next tick, so isRecording state val has a chance to update
    }
  }

  classifyLoop = async () => {
    if (!this.state.isRecording) return
    await this.classify()
    setTimeout( () => this.classifyLoop(), 0) // schedule a recusion on the next tick, so we have time to do GUI work like responding to the toggle button
  }

  classify = async () => {
    const imageSrc = this.webcamRef.current.getScreenshot();
    const { classLabels, predictions, highestProbabilityIndex } = await this.props.classifier.classify(imageSrc);
    let sortedClassLabels = classLabels.splice(0)
    sortedClassLabels.sort()
    this.setState({
      bestLabel: sortedClassLabels[highestProbabilityIndex]
    })
    console.log(sortedClassLabels[highestProbabilityIndex])
  }

  render() {
    return (
        <div>
          <Webcam
            audio={false}
            height={this.props.width}
            width={this.props.height}
            ref={this.webcamRef}
            screenshotFormat="image/jpeg"
            videoConstraints={this.videoConstraints}
          />

        <Form.Button onClick={this.toggleRecording}>
          {
            this.state.isRecording ? 'Stop' : 'Start' 
          } Recording
        </Form.Button>

        <Card style={{width: '224px'}}>
          <Image src={this.state.imageDataUrl} />

          <Card.Content>
            <Card.Header>
              { this.state.bestLabel ? this.state.bestLabel : "Loading..." }
            </Card.Header>

            <Card.Meta>
              { this.state.bestLabelScore ? this.state.bestLabelScore : "" }
            </Card.Meta>
          </Card.Content>
        </Card>
      </div>
    )
      }
}

export default WebcamLoopClassifer