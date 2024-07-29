import React from 'react'
import CategoryIcon from '@mui/icons-material/Category';
import InventoryIcon from '@mui/icons-material/Inventory';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import GroupsIcon from '@mui/icons-material/Groups';
import StoreIcon from '@mui/icons-material/Store';
import Card from './Card'
import { dataLine, dataBar } from '../../assets/chartData';
import { Line, Bar } from 'react-chartjs-2'
import { Chart as ChartJS, LineElement, BarElement, CategoryScale, LinearScale, PointElement} from 'chart.js'
ChartJS.register(LineElement, BarElement, CategoryScale, LinearScale, PointElement)

const Dashboardpage = () => {
  return (
    <div className='grow p-8'>
      <h2 className='text-2x1 mb-4'>Dashboard</h2>
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6'>
        <Card icon={<CategoryIcon />} title='Category' value={'140'} />
        <Card icon={<CheckCircleIcon />} title='Products' value={'120'} />
        <Card icon={<InventoryIcon />} title='Orders' value={'30'} />
        <Card icon={<GroupsIcon />} title='Users' value={'15'} />
        <Card icon={<StoreIcon />} title='Store' value={'500'} />
      </div>
      <div className=' grid grid-cols-1 lg:grid-cols-2 gap-4' >
        <div className='bg-white p-4 rounded-lg shadow-md'>
            <h3 className='text-lg font-semibold mb-4'>Sales Data</h3>
            <Line data = {dataLine} />
        </div>
        <div className=' grid grid-cols-1 lg:grid-cols-2'>
            <h3 className='text-lg font-semibold mb-4'>Products Data</h3>
            <Bar data = {dataBar} />
        </div>
      </div>
    </div>
  )
}

export default Dashboardpage
