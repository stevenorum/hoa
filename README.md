# hoa
SparkFun Artemis-based high-speed sound measurement. Named after those annoying people who make it necessary to worry about how much noise your long-distance holepunchers are making.

## Components

This is built around two SparkFun products, the [Artemis line of Arduino-compatible microcontrollers](https://www.sparkfun.com/artemis) and their [analog sound detector](https://www.sparkfun.com/products/12642). It also requires other stuff you probably have lying around (wire, USB-C cable, resistors or a potentiometer, soldering supplies).

## What's the goal?

All told it should be possible to build one of these  for ~$30 or so, which is several orders of magnitude cheaper than a commercial tool for measuring gunshot noise. That said, it's nowhere near as precise or general-purpose. It's specifically designed to compare the amplitude of different sounds when measured back-to-back in the same environment. It isn't necessarily going to be consistent across uses (due to the output being heavily dependent on the potentiometer setting and sensor placement relative to the muzzle) and it isn't calibrated to a standard scale (it doesn't measure in decibels and I don't know how doable it'd be to convert its measurement into decibels). However, for comparing the effect of different firearm setups (different suppressors, different powder loads, different firearms, etc.), it should be quite useful.
