import React from 'react'
import MUIDataTable from "mui-datatables";
import { createTheme, ThemeProvider } from '@mui/material/styles'

const columns = ["Name", "Company", "City", "State"];

const StoresPage =() => {

  const data = [
    ["Joe James", "Test Corp", "Yonkers", "NY"],
    ["John Walsh", "Test Corp", "Hartford", "CT"],
    ["Bob Herm", "Test Corp", "Tampa", "FL"],
    ["James Houston", "Test Corp", "Dallas", "TX"],
   ];
   
   const options = {
     selectableRows: 'false',
     elevation: 0,
     rowsPerPage: 5,
     rowsPerPageOptions: [5, 10, 20, 30]

   };

  const getMuiTheme = () =>
    createTheme ({
      typography: {
        fontFamily: 'Poppins'
      },
      palette: {
        background: {
          paper: '#1e293b',
          default: '#0f172a',
        }
      }
    })

  return (
    <div className='bg-slate-100 py-10 min-h-screen grid place-items-center'>
      <div className='w-10/12 max-w-4xl'>
      <ThemeProvider theme={getMuiTheme()}>
      <MUIDataTable
        title={"Stores List"}
        data={data}
        columns={columns}
        options={options}
      />
      </ThemeProvider>
      </div>
    </div>
  )
}

export default StoresPage;