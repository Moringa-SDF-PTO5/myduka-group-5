/* eslint-disable react/prop-types */
import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const SummaryPage = ({ title, value }) => (
  <Card>
    <CardContent>
      <Typography color="textSecondary" gutterBottom>
        {title}
      </Typography>
      <Typography variant="h5" component="h2">
        {value}
      </Typography>
    </CardContent>
  </Card>
);

export default SummaryPage
