import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { TextField, FormControl, InputLabel, Select, MenuItem, Button, Switch } from '@mui/material';
import { useDispatch } from 'react-redux';
import { addUser, editUser } from '../userSlice';

export default function EditForm({userDetails, onClose, isEdit, onSetEdit}) {
  const { reset, register, control, getValues, handleSubmit } = useForm();
  const dispatch = useDispatch()

  useEffect(function () {
    if (userDetails) {
      reset(userDetails);
    }
  }, [reset, userDetails]);

  function onSubmit(values) {
    if (isEdit) {
      dispatch(editUser(values))
    } else {
      dispatch(addUser({...values,id: new Date().getTime(), active:true, role:'Clerk'}))
    }
    onSetEdit(false)
    onClose()
  }

  return (
    <form onSubmit= { handleSubmit(onSubmit) } className='space-y-4 mt-2'>
      <TextField type='text' id="name" label="User Name" variant="outlined" fullWidth {...register('name')} />
      <TextField type='email' id="email" label="Email" variant="outlined" fullWidth {...register('email')} />
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Role</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={getValues('role') || ''}
          defaultValue={getValues('role') || ''}
          label="Role"
          {...register('role')}
        >
          <MenuItem value=''>Select Role</MenuItem>
          <MenuItem value='Admin'>Admin</MenuItem>
          <MenuItem value='Clerk'>Clerk</MenuItem>
          <MenuItem value='Merchant'>Merchant</MenuItem>
        </Select>
      </FormControl>
      <Controller
        name="active"
        control={control}
        defaultValue={!!getValues('active')}
        render={({ field }) => <Switch {...field} checked={field.value} />}
      />
      <Button type='submit' variant='contained' fullWidth>{isEdit ? 'Edit User' : 'Add User'}</Button>
    </form>
  );
}
